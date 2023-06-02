using Microsoft.AspNetCore.Mvc;
using NeuroMedicProject.Models;
using System.Text.Json;
namespace NeuroMedics;
public class HomeController : Controller
{
    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public ActionResult ProcessImage(IFormFile image)
    {
        var text = ImageHandlerModel.ReadTextFromFile("C:\\Users\\Тимур\\Desktop\\NeuroMedics\\wwwroot\\lib\\JSON.txt");
        var values = JsonSerializer.Deserialize<Dictionary<string, string>>(text);
        var imagePath = ImageHandlerModel.SaveFile(image);
        var result = ImageHandlerModel.ProcessImageFromFile(imagePath);
        return Content(result + "|" + values[result]);
    }
}