---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.33 ClearingDetails <ClrDtls>", "4.4.5.4.33.4 TradeCounterpartyIdentification <TradCtrPtyId>", "4.4.5.4.33.4.4 ReceivingParties <RcvgPties>", "4.4.5.4.33.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [189, 190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.33.4.4.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 189 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 189

```text
ContactPerson <CtctPrsn> contains the following elements (see ContactIdentification2 on page 458
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 459
   GivenName <GvnNm> [0..1] Text 459
   Name <Nm> [1..1] Text 459
   PhoneNumber <PhneNb> [0..1] Text 459
   MobileNumber <MobNb> [0..1] Text 459
   FaxNumber <FaxNb> [0..1] Text 459
   EmailAddress <EmailAdr> [0..1] Text 459
4.4.5.4.33.4.4.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
4.4.5.4.34  GrossAmount <GrssAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
GrossAmount <GrssAmt> contains the following elements (see AmountAndDirection21 on page 377
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
4.4.6 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C19 SupplementaryDataRule
SupplementaryData <SplmtryData> contains the following elements (see SupplementaryData1 on
page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 441
   Envelope <Envlp> [1..1] (External Schema) 441
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 189
```

## File page 190

```text
Constraints
• SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 190
```

