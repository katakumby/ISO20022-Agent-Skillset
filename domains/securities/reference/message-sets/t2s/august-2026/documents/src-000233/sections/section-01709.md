---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "63.4 Message Building Blocks", "63.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "63.4.2.2 IssuerInvestorCSD <IssrInvstrCSD>", "63.4.2.2.2 InvestorCSD <InvstrCSD>", "63.4.2.2.2.2 CombinedIdentification <CmbndId>"]
file_pages: [2357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 63.4.2.2.2.2 CombinedIdentification <CmbndId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2357 to 2357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2357

```text
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
63.4.2.2.2.2  CombinedIdentification <CmbndId>
Presence: [1..1]
Definition: Identifies the party with the combined identification of both the responsible entity and the
party itself.
CombinedIdentification <CmbndId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
63.4.2.3  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
63.4.3 Update <Upd>
Presence: [1..1]
Definition: Provides data that needs to be maintained.
Update <Upd> contains the following SecurityCSDLinkUpdate3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DefaultLink <DfltLk> [0..1] Indicator 2357
   ValidTo <VldTo> [1..1] ± 2358
63.4.3.1  DefaultLink <DfltLk>
Presence: [0..1]
Definition: Specifies whether the security CSD link is the default link.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities 2357 August 2026
```

