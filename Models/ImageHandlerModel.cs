using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;

namespace NeuroMedicProject.Models
{
    public class ImageHandlerModel
    {
        public static string ProcessImageFromFile(string imagePath)
        {
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "C:/Users/Тимур/AppData/Local/Programs/Python/Python311/python.exe";
            var script = "C:/Users/Тимур/Desktop/our-AI-project-ai-model/script.py";
            var newImagePath = imagePath.Replace(@"\\", "/");
            psi.Arguments = string.Format("{0} {1}", script, newImagePath);
            psi.UseShellExecute = false;
            psi.RedirectStandardOutput = true;
            var errors = "";
            var result = "";
            using(var process = Process.Start(psi))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result += "Экзема";
                }
            }
            return result; 
        }
        public static string SaveFile(IFormFile file)
        {
            if (file == null || file.Length == 0)
            {
                throw new ArgumentException("File is empty");
            }

            string fileName = Guid.NewGuid().ToString() + Path.GetExtension(file.FileName);
            string path = Path.Combine(@"C:\Users\Тимур\Desktop\NeuroMedics", "uploads", fileName);

            using (var stream = new FileStream(path, FileMode.Create))
            {
                file.CopyToAsync(stream);
            }

            return path;
            
        }
        public static string ReadTextFromFile(string path)
        {
            return File.ReadAllText(path);
        }
    }
}