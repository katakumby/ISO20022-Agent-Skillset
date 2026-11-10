---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.7 SettlementDetails <SttlmDtls>", "2.4.7.2 Depository <Dpstry>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.7.2 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

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
2.4.7.2  Depository <Dpstry>
Presence: [0..1]
Definition: Place where settlement of the securities takes place.
Depository <Dpstry> contains one of the following elements (see PartyIdentification255Choice on
page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 454
Or   NameAndAddress <NmAndAdr> [1..1] ± 454
Or}   Country <Ctry> [1..1] CodeSet   'C5 454
2.4.8 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C18 SupplementaryDataRule
SupplementaryData <SplmtryData> contains the following elements (see SupplementaryData1 on
page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 441
   Envelope <Envlp> [1..1] (External Schema) 441
Constraints
• SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 63
```

