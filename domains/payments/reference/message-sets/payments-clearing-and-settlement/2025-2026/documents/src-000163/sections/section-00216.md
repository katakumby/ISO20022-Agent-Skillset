---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.20 ChargeBearer <ChrgBr>"]
file_pages: [317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.20 ChargeBearer <ChrgBr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 317 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 317

```text
4.4.3.20  ChargeBearer <ChrgBr>
Presence: [0..1]
Definition: Specifies which party/parties will bear the charges associated with the processing of the
payment transaction.
Usage: The ChargeBearer applies to the return message, not to the original instruction.
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
4.4.3.21  ChargesInformation <ChrgsInf>
Presence: [0..*]
Definition: Provides information on the charges to be paid by the charge bearer(s) related to the
processing of the return transaction.
ChargesInformation <ChrgsInf> contains the following Charges16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C12 317
   Agent <Agt> [1..1] ± 318
   Type <Tp> [0..1]  318
{Or     Code <Cd> [1..1] CodeSet 319
Or}     Proprietary <Prtry> [1..1] ± 319
4.4.3.21.1  Amount <Amt>
Presence: [1..1]
Definition: Transaction charges to be paid by the charge bearer.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
317 March 2026
```

