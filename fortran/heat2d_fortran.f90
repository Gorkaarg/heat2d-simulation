program heat2d_fortran
  implicit none

  integer, parameter :: Nx = 50, Ny = 50
  real(8), parameter :: Lx = 1.0d0, Ly = 1.0d0
  real(8), parameter :: alpha = 1.0d0
  real(8) :: dx, dy, dt
  integer, parameter :: Nt = 300
  integer :: i, j, n, rep, reps

  real(8), dimension(Nx, Ny) :: u, un
  real(8) :: x, y

  integer :: start, finish, rate
  real(8) :: tiempo_total, tiempo_por_simulacion

  reps = 1000   ! solo para medir, no afecta a la simulación real

  dx = Lx / real(Nx - 1, 8)
  dy = Ly / real(Ny - 1, 8)
  dt = 0.25d0 * min(dx, dy)**2 / alpha

  ! Condición inicial (solo una vez)
  do j = 1, Ny
    y = (real(j - 1, 8) * dy)
    do i = 1, Nx
      x = (real(i - 1, 8) * dx)
      u(i, j) = exp(-50.d0 * ((x - 0.5d0)**2 + (y - 0.5d0)**2))
    end do
  end do

  ! Medición precisa
  call system_clock(count_rate=rate)
  call system_clock(start)

  do rep = 1, reps
    un = u
    do n = 1, Nt
      do j = 2, Ny - 1
        do i = 2, Nx - 1
          u(i, j) = un(i, j) + alpha * dt * ( &
            (un(i+1, j) - 2.d0*un(i, j) + un(i-1, j)) / dx**2 + &
            (un(i, j+1) - 2.d0*un(i, j) + un(i, j-1)) / dy**2 )
        end do
      end do
    end do
  end do

  call system_clock(finish)

  tiempo_total = real(finish - start, 8) / real(rate, 8)
  tiempo_por_simulacion = tiempo_total / reps

  print *, "Tiempo total:", tiempo_total, "segundos"
  print *, "Tiempo por simulación:", tiempo_por_simulacion, "segundos"

end program heat2d_fortran

