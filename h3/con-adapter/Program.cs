namespace H3.ConAdapter;

public class Encomienda
{
    public string CodigoSeguimiento { get; set; } = string.Empty;
    public decimal Peso { get; set; }
}

public interface ISistemaSeguimiento
{
    void RegistrarMovimiento(string codigo, string ubicacion);
}

public class ExternalAerolineaApi
{
    public void TrackFlightCargo(string trackingNum, string airportCode, DateTime timestamp)
    {
        Console.WriteLine($"[AEROLÍNEA] Carga {trackingNum} registrada en aeropuerto {airportCode} el {timestamp}");
    }
}

public class AerolineaAdapter : ISistemaSeguimiento
{
    private readonly ExternalAerolineaApi _apiExterna;

    public AerolineaAdapter(ExternalAerolineaApi apiExterna)
    {
        _apiExterna = apiExterna;
    }

    public void RegistrarMovimiento(string codigo, string ubicacion)
    {
        _apiExterna.TrackFlightCargo(codigo, ubicacion, DateTime.Now);
    }
}
