import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { finalize, map, Observable, take, timer } from 'rxjs';

@Component({
  selector: 'app-page-not-found',
  templateUrl: './page-not-found.component.html',
  styleUrls: ['./page-not-found.component.scss'],
})
export class PageNotFoundComponent {
  redirectTimeRemaining: number = 5;
  redirectTimer$!: Observable<number>;

  constructor(private router: Router) {}

  ngOnInit(): void {
    this.redirectTimer$ = timer(0, 1000).pipe(
      take(this.redirectTimeRemaining),
      map((x) => this.redirectTimeRemaining - (x + 1)),
      finalize(() => this.router.navigate(['']))
    );
  }
}
