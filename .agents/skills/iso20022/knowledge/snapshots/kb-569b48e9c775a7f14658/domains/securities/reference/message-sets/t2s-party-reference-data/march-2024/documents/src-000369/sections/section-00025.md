---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.3 ReturnCriteria <RtrCrit>", "3.4.3.1 OpeningDate <OpngDt>"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.3.1 OpeningDate <OpngDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
ReturnCriteria <RtrCrit> contains the following PartyDataReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1] Indicator 31
   ClosingDate <ClsgDt> [0..1] Indicator 31
   Type <Tp> [0..1] Indicator 31
   PartyIdentification <PtyId> [0..1] Indicator 32
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] Indicator 32
   RestrictionIdentification <RstrctnId> [0..1] Indicator 32
   RestrictedOnDate <RstrctdOnDt> [0..1] Indicator 32
   Name <Nm> [0..1] Indicator 32
   ShortName <ShrtNm> [0..1] Indicator 33
   Address <Adr> [0..1] Indicator 33
   TechnicalAddress <TechAdr> [0..1] Indicator 33
   ContactDetails <CtctDtls> [0..1] Indicator 33
   ResidenceType <ResTp> [0..1] Indicator 33
   LockStatus <LckSts> [0..1] Indicator 34
   MarketSpecificAttribute <MktSpcfcAttr> [0..1] Indicator 34
3.4.3.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Indicates whether the opening date of the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Indicates whether the closing date of the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 186):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.3  Type <Tp>
Presence: [0..1]
Definition: Indicates whether the type is requested.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
31 March 2024
```

