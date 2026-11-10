---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.3 AggregatedEntry <AggtdNtry>", "4.4.2.14.17.3.2 TransactionCategory <TxCtgy>"]
file_pages: [611]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.3.2 TransactionCategory <TxCtgy>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 611 to 611.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 611

```text
CodeName Name Definition
LOYT Loyalty Loyalty services.
NRES NoShow No show after reservation.
PUCO PurchaseCorporate Purchase and corporate data.
RECP RecurringPayment Recurring payment.
SOAF SolicitedAvailableFunds Solicited available funds.
UNAF UnsolicitedAvailableFunds Unsolicited available funds.
VCAU VoiceAuthorisation Voice authorisation.
4.4.2.14.17.3.2  TransactionCategory <TxCtgy>
Presence: [0..1]
Definition: Category code conform to ISO 18245, related to the type of services or goods the merchant
provides for the transaction.
Datatype: "ExternalCardTransactionCategory1Code" on page 894
4.4.2.14.17.3.3  SaleReconciliationIdentification <SaleRcncltnId>
Presence: [0..1]
Definition: Unique identification of the sales reconciliation period between the acceptor and the acquirer.
This identification might be linked to the identification of the settlement for further verification by the
merchant.
Datatype: "Max35Text" on page 916
4.4.2.14.17.3.4  SequenceNumberRange <SeqNbRg>
Presence: [0..1]
Definition: Range of sequence numbers on which the globalisation applies.
SequenceNumberRange <SeqNbRg> contains the following CardSequenceNumberRange1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FirstTransaction <FrstTx> [0..1] Text 611
   LastTransaction <LastTx> [0..1] Text 611
4.4.2.14.17.3.4.1  FirstTransaction <FrstTx>
Presence: [0..1]
Definition: CardSequenceNumberRange1: FirstTransactionSequenceNumberMessage element to be
finalised once feedback from Card SEG has been received.
Datatype: "Max35Text" on page 916
4.4.2.14.17.3.4.2  LastTransaction <LastTx>
Presence: [0..1]
Definition: CardSequenceNumberRange1: LastTransactionSequenceNumberMessage element to be
finalised once feedback from Card SEG has been received.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
611 March 2026
```

