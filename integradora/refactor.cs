namespace Integradora.Comedor;

using System;
using System.Collections.Generic;

// CURA DE OCP (Open/Closed Principle)

// Se separa la asignacion de precios en una clase aparte para agregar o cambiar menus sin modificar GestorDePedidos

public class CalculadorTarifas
{
    private readonly Dictionary<string, decimal> _precios = new(StringComparer.OrdinalIgnoreCase)
    {
        { "estandar", 12m },
        { "vegetariano", 14m },
        { "beca", 5m }
    };

    public decimal ObtenerPrecioBase(string tipoMenu)
    {
        return _precios.TryGetValue(tipoMenu, out var precio) ? precio : 12m;
    }
}

public class GestorDePedidos
{
    private readonly CalculadorTarifas _calculador = new();

    public void ProcesarPedido(string estudiante, string tipoMenu, int cantidad)
    {
        // Se elimina el switch y se usa CalculadorTarifas para calcular los precios.
        decimal precioBase = _calculador.ObtenerPrecioBase(tipoMenu);
        decimal total = precioBase * cantidad;

        var baseDeDatos = new BaseDeDatosComedor();
        baseDeDatos.GuardarPedido(estudiante, tipoMenu, cantidad, total);

        Console.WriteLine("----- VALE DE COMEDOR -----");
        Console.WriteLine($"{estudiante}: {cantidad} x menú {tipoMenu}");
        Console.WriteLine($"TOTAL: {total:0.00} Bs");

        var correo = new CorreoUniversitario();
        correo.Enviar($"Pedido registrado: {cantidad} x {tipoMenu}, {estudiante}");
    }
}

public class BaseDeDatosComedor
{
    public void GuardarPedido(string estudiante, string menu, int cantidad, decimal total)
        => Console.WriteLine($"[BD] INSERT INTO pedidos VALUES ('{estudiante}', '{menu}', {cantidad}, {total})");
}

public class CorreoUniversitario
{
    public void Enviar(string mensaje) => Console.WriteLine($"[CORREO] {mensaje}");
}

public static class Demo
{
    public static void Correr()
    {
        new GestorDePedidos().ProcesarPedido("Noelia", "vegetariano", 2);
    }
}
