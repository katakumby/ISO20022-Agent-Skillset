---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>", "2.4.2.19.7.2 ChequeNumber <ChqNb>"]
file_pages: [57]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7.2 ChequeNumber <ChqNb>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 57 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
CodeName Name Definition
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
early payment from any bank under
subtraction of a discount. The ordering
customer's account is debited on value
date.
ELDR ElectronicDraft An instrument with a future value date
(do not pay before], which in commercial
terms is a 'negotiatable instrument': the
beneficiary can receive early payment
from any bank under subtraction of a
discount. The ordering customer's
account is debited on value date.
2.4.2.19.7.2  ChequeNumber <ChqNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a cheque as assigned by the agent.
Datatype: "Max35Text" on page 609
2.4.2.19.7.3  ChequeFrom <ChqFr>
Presence: [0..1]
Definition: Identifies the party that ordered the issuance of the cheque.
ChequeFrom <ChqFr> contains the following NameAndAddress18 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 57
   Address <Adr> [1..1] ± 58
2.4.2.19.7.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and is usually used to identify that party.
Datatype: "Max140Text" on page 608
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 57 March 2026
```

