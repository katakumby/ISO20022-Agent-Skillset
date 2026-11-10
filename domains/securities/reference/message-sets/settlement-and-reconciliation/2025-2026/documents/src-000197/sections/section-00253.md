---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.12 Payment <Pmt>"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.12 Payment <Pmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
10.4.6.12  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
10.4.6.13  Status <Sts>
Presence: [0..1]
Definition: Status of the allegement.
Status <Sts> contains one of the following elements (see "AllegementStatus3Choice" on page 1871 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1871
Or}   Proprietary <Prtry> [1..1] ± 1872
10.4.6.14  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction has been executed.
PlaceOfTrade <PlcOfTrad> contains the following elements (see "PlaceOfTradeIdentification1" on
page 1527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C27 1527
   LEI <LEI> [0..1] IdentifierSet 1527
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 383 March 2026
```

