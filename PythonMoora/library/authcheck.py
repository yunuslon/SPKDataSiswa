from orm.models import SoalBiologi,SoalFisika,SoalKimia,SoalMatematika

class AuthCheck:

    @staticmethod
    def isSuperUser(user):
        if user.is_superuser:
            return True
        else:
            return False
    @staticmethod
    def isSoalBio(user):
        if user.is_staff:
            try:
                user.soalbiologi
                return True
            except SoalBiologi.DoesNotExist:
                return False
        else:
            return False
    @staticmethod
    def isSoalFis(user):
        if user.is_staff:
            try:
                user.soalfisika
                return True
            except SoalFisika.DoesNotExist:
                return False
        else:
            return False
    @staticmethod
    def isSoalKim(user):
        if user.is_staff:
            try:
                user.soalkimia
                return True
            except SoalKimia.DoesNotExist:
                return False
        else:
            return False
    @staticmethod
    def isSoalMat(user):
        if user.is_staff:
            try:
                user.soalmatematika
                return True
            except SoalMatematika.DoesNotExist:
                return False
        else:
            return False
    