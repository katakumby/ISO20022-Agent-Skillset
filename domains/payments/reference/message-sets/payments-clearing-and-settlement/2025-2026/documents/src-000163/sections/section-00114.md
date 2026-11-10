---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.9 ChargeBearer <ChrgBr>"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.9 ChargeBearer <ChrgBr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
Definition: Factor used to convert an amount from one currency into another. This reflects the price at
which one currency was bought with another currency.
Datatype: "BaseOneRate" on page 1242
3.4.2.9  ChargeBearer <ChrgBr>
Presence: [1..1]
Definition: Specifies which party/parties will bear the charges associated with the processing of the
payment transaction.
Datatype: "ChargeBearerType1Code" on page 1225
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
3.4.2.10  ChargesInformation <ChrgsInf>
Presence: [0..*]
Definition: Provides information on the charges to be paid by the charge bearer(s) related to the
payment transaction.
ChargesInformation <ChrgsInf> contains the following Charges16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C11 163
   Agent <Agt> [1..1] ± 164
   Type <Tp> [0..1]  164
{Or     Code <Cd> [1..1] CodeSet 165
Or}     Proprietary <Prtry> [1..1] ± 165
3.4.2.10.1  Amount <Amt>
Presence: [1..1]
Definition: Transaction charges to be paid by the charge bearer.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
163 March 2026
```

