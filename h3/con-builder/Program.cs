namespace H3.ConBuilder;

public class Encomienda
{
    public string CodigoSeguimiento { get; set; } = string.Empty;
    public decimal Peso { get; set; }
    public string Tipo { get; set; } = string.Empty;
    public decimal CostoEnvio { get; set; }
    public List<string> PuntosDeControl { get; set; } = new();
    public string? FirmaDigital { get; set; }
    public bool EsFragil { get; set; }
}

public class EncomiendaBuilder
{
    private readonly Encomienda _encomienda = new();

    public EncomiendaBuilder ConDatosBasicos(string codigo, decimal peso, string tipo)
    {
        _encomienda.CodigoSeguimiento = codigo;
        _encomienda.Peso = peso;
        _encomienda.Tipo = tipo;
        return this;
    }

    public EncomiendaBuilder ConCosto(decimal costo)
    {
        _encomienda.CostoEnvio = costo;
        return this;
    }

    public EncomiendaBuilder AgregarPuntoControl(string punto)
    {
        _encomienda.PuntosDeControl.Add(punto);
        return this;
    }

    public EncomiendaBuilder MarcarComoFragil()
    {
        _encomienda.EsFragil = true;
        return this;
    }

    public EncomiendaBuilder ConFirmaDigital(string firma)
    {
        _encomienda.FirmaDigital = firma;
        return this;
    }

    public Encomienda Build() => _encomienda;
}
