from users.models import Role, Menu, Permission, MenuRole, User
from django.contrib.auth.hashers import make_password

# Clear existing data (optional)
Role.objects.all().delete()
Menu.objects.all().delete()
Permission.objects.all().delete()
MenuRole.objects.all().delete()
User.objects.all().delete()

# Create Roles
admin_role = Role.objects.create(name="Admin")
dosen_role = Role.objects.create(name="Dosen")
mahasiswa_role = Role.objects.create(name="Mahasiswa")

# Create Menus
dashboard = Menu.objects.create(name="Dashboard", path="/dashboard")
formulir = Menu.objects.create(name="Formulir", path="/formulir")
data_mahasiswa = Menu.objects.create(name="Data Mahasiswa", path="/data-mahasiswa")

# Create Permissions
perm_view = Permission.objects.create(code="view", description="Lihat data")
perm_add = Permission.objects.create(code="add", description="Tambah data")
perm_edit = Permission.objects.create(code="edit", description="Ubah data")
perm_delete = Permission.objects.create(code="delete", description="Hapus data")

# Assign MenuRole
mr1 = MenuRole.objects.create(role=admin_role, menu=dashboard)
mr1.permissions.set([perm_view, perm_add, perm_edit, perm_delete])

mr2 = MenuRole.objects.create(role=admin_role, menu=data_mahasiswa)
mr2.permissions.set([perm_view, perm_edit])

mr3 = MenuRole.objects.create(role=mahasiswa_role, menu=formulir)
mr3.permissions.set([perm_view, perm_add])

# Create User admin
User.objects.create(
    username="admin",
    password=make_password("admin123"),
    email="admin@matana.ac.id",
    first_name="Admin",
    last_name="Super",
    role=admin_role,
    is_superuser=True,
    is_staff=True,
)

print("✅ Data dummy berhasil dibuat.")
