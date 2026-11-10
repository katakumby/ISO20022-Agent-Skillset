---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.4 UnderlyingSecurity <UndrlygScty>", "5.4.6.4.2 PlaceOfListing <PlcOfListg>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.4.2 PlaceOfListing <PlcOfListg>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
5.4.6.4.2  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Place where the referenced financial instrument is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 883 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 884
Or}   Description <Desc> [1..1] Text 884
5.4.6.4.3  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the financial instrument.
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 976
Or}   Proprietary <Prtry> [1..1] ± 979
5.4.6.4.4  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI).
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 888 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 888
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 888
5.4.6.4.5  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a financial instrument is currently denominated.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 289 February 2026
```

