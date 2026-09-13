namespace H3.ConFactory;

public class Encomienda
{
    public string CodigoSeguimiento { get; set; } = string.Empty;
    public decimal Peso { get; set; }
    public string Tipo { get; set; } = string.Empty;
    public decimal CostoEnvio { get; set; }
}

public abstract class EncomiendaFactory
{
    public abstract Encomienda CrearEncomienda(string codigo, decimal peso);
}

public class EncomiendaEstandarFactory : EncomiendaFactory
{
    public override Encomienda CrearEncomienda(string codigo, decimal peso)
    {
        return new Encomienda
        {
            CodigoSeguimiento = codigo,
            Peso = peso,
            Tipo = "Estandar",
            CostoEnvio = peso * 8.0m
        };
    }
}

public class EncomiendaExpressFactory : EncomiendaFactory
{
    public override Encomienda CrearEncomienda(string codigo, decimal peso)
    {
        return new Encomienda
        {
            CodigoSeguimiento = codigo,
            Peso = peso,
            Tipo = "Express",
            CostoEnvio = peso * 15.0m
        };
    }
}

public class EncomiendaInternacionalFactory : EncomiendaFactory
{
    public override Encomienda CrearEncomienda(string codigo, decimal peso)
    {
        return new Encomienda
        {
            CodigoSeguimiento = codigo,
            Peso = peso,
            Tipo = "Internacional",
            CostoEnvio = peso * 30.0m
        };
    }
}
