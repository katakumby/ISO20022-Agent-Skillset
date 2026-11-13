---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.15 AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>", "11.4.6.2.15.9 SettlementDate <SttlmDt>"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.15.9 SettlementDate <SttlmDt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
SettlementAmount <SttlmAmt> contains the following elements (see AmountAndDirection27 on
page 379 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C1,
  'C7
379
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 380
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount   'C2,
  'C6
380
   ForeignExchangeDetails <FXDtls> [0..1] ± 381
11.4.6.2.15.9  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Provides the contractual settlement date.
Datatype: ISODate on page 487
11.4.6.2.15.10  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Indicates if the obligation will result in a receive or a delivery of securities.
Datatype: ReceiveDelivery1Code on page 481
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
11.4.6.2.15.11  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled.
Datatype: DeliveryReceiptType2Code on page 477
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
11.4.6.2.15.12  References <Refs>
Presence: [0..1]
Definition: Provides the references of the underlying trade leg(s) and/or the reference to the related net
position message.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 366
```

