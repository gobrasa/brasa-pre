import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-mentor-list',
  templateUrl: './mentor-list.component.html'
})

export class MentorListComponent {
  @Input() items: any[] = [];
  @Input() listName: string;
  @Input() navigateTo: any;
}
