import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpenseDeleteComponent } from './expense-delete.component';

describe('ExpenseDeleteComponent', () => {
  let component: ExpenseDeleteComponent;
  let fixture: ComponentFixture<ExpenseDeleteComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExpenseDeleteComponent]
    });
    fixture = TestBed.createComponent(ExpenseDeleteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
