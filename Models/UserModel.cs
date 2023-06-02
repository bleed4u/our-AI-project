using System.Collections.Generic;

namespace NeuroMedicProject.Models
{
    public class UserModel
    {
        public int Id { get; set; }
        public string Username { get; set; }
        public string Password { get; set; }

        // Метод для получения истории запросов, если необходимо
    }
}