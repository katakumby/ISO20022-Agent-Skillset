---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.14 DateType4Code"]
file_pages: [502]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.14 DateType4Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 502 to 502.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 502

```text
Type: CodeSet
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.2.2.14  DateType4Code
Definition: Specifies a type of date.
Type: CodeSet
CodeName Name Definition
OPEN Open Open-dated, which indicates that the
date has not been established.
UKWN Unknown Date is unknown by the sender or has
not been established.
7.2.2.15  DeliveryReceiptType2Code
Definition: Specifies how the transaction is to be settled.
Type: CodeSet
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
7.2.2.16  DeliveryReturn1Code
Definition: Specifies the type of delivery return.
Type: CodeSet
CodeName Name Definition
UNRE UnrecognisedDelivery Original delivery is not recognized.
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
DMON WrongSettlementAmount Wrong settlement amount settled in the
original delivery.
PART PartialDelivery Only a portion of the original transaction
quantity was delivered by the Central
Securities Depository (CSD).
SAFE AccountMissing Account information is missing in the
original delivery.
DUEB DueBiillMissing Due bill information missing in the
original delivery.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 502 March 2026
```

