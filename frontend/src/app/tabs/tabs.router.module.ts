import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TabsPage } from './tabs.page';
import { MenteeDetailPage } from '../mentee/mentee-detail/mentee-detail.page';
import { MenteePage } from '../mentee/mentee/mentee.page';
//import { ContactPage } from '../contact/contact.page';
//import { CardDeckPage } from '../card/card-deck/card-deck.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      {
        path: 'mentee',
        component: MenteePage
      },
      {
        path: 'mentor',
        component: MenteeDetailPage
      },
      {
        path: 'informacoes',
        component: MenteeDetailPage
      },{
        path: 'mentee/detail',
        component: MenteeDetailPage
      }
      /*
      {
        path: 'about',
        outlet: 'about',
        component: AboutPage
      },
      {
        path: 'contact',
        outlet: 'contact',
        component: ContactPage
      },
      {
        path: 'card',
        outlet: 'card',
        component: CardDeckPage
      },
      {
        path: 'card/:cardId',
        outlet: 'card',
        component: CardDetailPage
      },
      {
        path: '/mentee/1',
        outlet: 'card',
        component: CardDetailPage
      },
      {
        path: 'card/:cardDeckGroup/:cardDeck',
        outlet: 'card',
        component: CardListingPage
      }
      */
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TabsPageRoutingModule {}
