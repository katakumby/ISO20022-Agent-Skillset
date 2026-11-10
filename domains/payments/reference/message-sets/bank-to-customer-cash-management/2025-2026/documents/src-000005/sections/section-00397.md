---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.14 Charges <Chrgs>", "4.4.2.14.14.2 Record <Rcrd>", "4.4.2.14.14.2.4 Type <Tp>", "4.4.2.14.14.2.4.2 Proprietary <Prtry>"]
file_pages: [595]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.14.2.4.2 Proprietary <Prtry>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 595 to 595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 595

```text
4.4.2.14.14.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 838 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 839
   Issuer <Issr> [0..1] Text 839
4.4.2.14.14.2.5  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charge or fee.
Datatype: "PercentageRate" on page 913
4.4.2.14.14.2.6  Bearer <Br>
Presence: [0..1]
Definition: Specifies which party/parties will bear the charges associated with the processing of the
payment transaction.
Datatype: "ChargeBearerType1Code" on page 890
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
4.4.2.14.14.2.7  Agent <Agt>
Presence: [0..1]
Definition: Agent that takes the transaction charges or to which the transaction charges are due.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
595 March 2026
```

