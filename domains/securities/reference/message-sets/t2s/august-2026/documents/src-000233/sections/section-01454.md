---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.3 ReturnCriteria <RtrCrit>", "35.4.3.1 OpeningDate <OpngDt>"]
file_pages: [2068]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.3.1 OpeningDate <OpngDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2068 to 2068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2068

```text
ReturnCriteria <RtrCrit> contains the following PartyDataReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1] Indicator 2068
   ClosingDate <ClsgDt> [0..1] Indicator 2068
   Type <Tp> [0..1] Indicator 2068
   PartyIdentification <PtyId> [0..1] Indicator 2069
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] Indicator 2069
   RestrictionIdentification <RstrctnId> [0..1] Indicator 2069
   RestrictedOnDate <RstrctdOnDt> [0..1] Indicator 2069
   Name <Nm> [0..1] Indicator 2069
   ShortName <ShrtNm> [0..1] Indicator 2070
   Address <Adr> [0..1] Indicator 2070
   TechnicalAddress <TechAdr> [0..1] Indicator 2070
   ContactDetails <CtctDtls> [0..1] Indicator 2070
   ResidenceType <ResTp> [0..1] Indicator 2070
   LockStatus <LckSts> [0..1] Indicator 2071
   MarketSpecificAttribute <MktSpcfcAttr> [0..1] Indicator 2071
35.4.3.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Indicates whether the opening date of the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.2  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Indicates whether the closing date of the party is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.3  Type <Tp>
Presence: [0..1]
Definition: Indicates whether the type is requested.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2068 August 2026
```

