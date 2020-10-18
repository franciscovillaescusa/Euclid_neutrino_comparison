
#include <gsl/gsl_rng.h>

double GrowthFactor(double astart, double aend);
void   print_spec(void);
int    FatalError(int errnum);
void   displacement_fields(void);
void   initialize_ffts(void);
void   set_units(void);
void   assemble_particles(void);
void   free_ffts(void);
double fnl(double x);

int find_files(char *fname);

void   assemble_grid(void);
void   read_power_table(void);
double periodic_wrap(double x);

void read_growth_file(void);
double Growth_Tabulated(double k);
double BGrowth_Tabulated(double k);
double CDMGrowth_Tabulated(double k);
double NUGrowth_Tabulated(double k);


double PowerSpec(double kmag);
double PowerSpec_Efstathiou(double k);
double PowerSpec_EH(double k);
double PowerSpec_Tabulated(double k);
double PowerSpec_TOTAL(double k);
double PowerSpec_DM_2ndSpecies(double k);
double PowerSpec_Tabulated2nd(double k);
double PowerSpec_Tabulated_b(double k);

void   initialize_powerspectrum(void);
double GrowthFactor(double astart, double aend);
double growth(double a);
double growth_int(double);
double qromb(double (*func)(double), double a, double b);
double sigma2_int(double k);
double TopHatSigma2(double R);
double F_Omega(double a);

void   combine_particle_data(void);
int    compare_logk(const void *a, const void *b);


void  write_particle_data(void);
void  read_parameterfile(char *fname);
void  read_glass(char *fname);


double tk_eh(double k);

size_t my_fread(void *ptr, size_t size, size_t nmemb, FILE * stream);
size_t my_fwrite(void *ptr, size_t size, size_t nmemb, FILE * stream);

void save_local_data(void);
void add_WDM_thermal_speeds(float *vel);

int compare_type(const void *a, const void *b);

double get_fermi_dirac_vel_nu(void);
void fermi_dirac_init_nu(void);
void add_NU_thermal_speeds(float *vel);

#ifdef OUTPUT_DF
void write_density_field_data(void);
#endif 
