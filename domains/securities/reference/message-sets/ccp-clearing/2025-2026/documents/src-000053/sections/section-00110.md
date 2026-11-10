---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.12 SettlementDate <SttlmDt>", "4.4.5.4.12.1 Date <Dt>"]
file_pages: [149, 150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.12.1 Date <Dt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 149 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
4.4.5.4.12.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: ISODate on page 487
4.4.5.4.12.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 149
Or}   Proprietary <Prtry> [1..1] ± 149
4.4.5.4.12.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
4.4.5.4.12.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
4.4.5.4.13  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Provides details about the security identification.
Impacted by:   'C11 DescriptionPresenceRule  ', C12 DescriptionUsageRule, C13 ISINGuideline,
  'C14 ISINPresenceRule  ',   'C17 OtherIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 149
```

## File page 150

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
SecurityIdentification48 on page 391 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 392
   OtherIdentification <OthrId> [0..*]  392
     Identification <Id> [1..1] Text 392
     Suffix <Sfx> [0..1] Text 393
     Type <Tp> [1..1] ± 393
   Description <Desc> [0..1] Text 393
Constraints
• DescriptionPresenceRule
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
• DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
• ISINGuideline
(Rule)
When a ISIN code exist. It is strongly recommended that the ISIN be used.
• ISINPresenceRule
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 150
```

