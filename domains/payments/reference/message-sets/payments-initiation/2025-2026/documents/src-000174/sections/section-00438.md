---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.3 CodeSet", "6.2.3.8 ChequeType2Code"]
file_pages: [589]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.3.8 ChequeType2Code

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 589 to 589.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 589

```text
CodeName Name Definition
MLDB MailToDebtor Cheque is to be sent through mail
services to debtor.
MLCD MailToCreditor Cheque is to be sent through mail
services to creditor.
MLFA MailToFinalAgent Cheque is to be sent through mail
services to creditor agent.
CRDB CourierToDebtor Cheque is to be sent through courier
services to debtor.
CRCD CourierToCreditor Cheque is to be sent through courier
services to creditor.
CRFA CourierToFinalAgent Cheque is to be sent through courier
services to creditor agent.
PUDB PickUpByDebtor Cheque will be picked up by the debtor.
PUCD PickUpByCreditor Cheque will be picked up by the creditor.
PUFA PickUpByFinalAgent Cheque will be picked up by the creditor
agent.
RGDB RegisteredMailToDebtor Cheque is to be sent through registered
mail services to debtor.
RGCD RegisteredMailToCreditor Cheque is to be sent through registered
mail services to creditor.
RGFA RegisteredMailToFinalAgent Cheque is to be sent through registered
mail services to creditor agent.
6.2.3.8  ChequeType2Code
Definition: Specifies the type of cheque.
Type: CodeSet
CodeName Name Definition
CCHQ CustomerCheque Cheque drawn on the account of the
debtor, and debited on the debtor's
account when the cheque is cashed.
Synonym is 'corporate cheque'.
CCCH CertifiedCustomerCheque Cheque drawn on the account of the
debtor, and debited on the debtor's
account when the cheque is cashed. The
financial institution prints and certifies
the cheque, guaranteeing the payment.
BCHQ BankCheque Cheque drawn on the account of the
debtor's financial institution, which is
debited on the debtor's account when
the cheque is issued.These cheques are
printed by the debtor's financial
institution and payment is guaranteed by
the financial institution. Synonym is
'cashier's cheque'.
DRFT Draft A guaranteed bank cheque with a future
value date (do not pay before], which in
commercial terms is a 'negotiatable
instrument': the beneficiary can receive
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 589 March 2026
```

