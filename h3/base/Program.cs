namespace H3.Base;


public class Encomienda
{
    public string CodigoSeguimiento { get; set; } = string.Empty;
    public decimal Peso { get; set; }
    public string Tipo { get; set; } = string.Empty; 
    public decimal CostoEnvio { get; set; }
}

public class PuntoDeControl
{
    public string Ubicacion { get; set; } = string.Empty;
    public DateTime FechaHora { get; set; }
}

public class Entrega
{
    public string Destinatario { get; set; } = string.Empty;
    public string FirmaDigital { get; set; } = string.Empty;
}

public class ServicioEncomienda
{
    public Encomienda CrearEncomiendaDirecta(string codigo, decimal peso, string tipo)
    {
        var encomienda = new Encomienda
        {
            CodigoSeguimiento = codigo,
            Peso = peso,
            Tipo = tipo
        };

        if (tipo == "Express")
            encomienda.CostoEnvio = peso * 15.0m;
        else if (tipo == "Internacional")
            encomienda.CostoEnvio = peso * 30.0m;
        else
            encomienda.CostoEnvio = peso * 8.0m;

        return encomienda;
    }
}
