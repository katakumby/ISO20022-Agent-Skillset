---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.4 Message Building Blocks", "62.4.2 SecurityCSDLink <SctyCSDLk>"]
file_pages: [2343]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.4.2 SecurityCSDLink <SctyCSDLk>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2343 to 2343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2343

```text
62.4.2 SecurityCSDLink <SctyCSDLk>
Presence: [1..*]
Definition: This Securities CSD Link logical entity shall assign a security to a CSD in T2S in order to
define the eligibility of the instrument for settlement in that CSD. An attribute within this entity shall
specify which CSD is responsible for maintaining the instrument static data.
SecurityCSDLink <SctyCSDLk> contains the following SecurityCSDLink12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C9
2343
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2344
{Or     IssuerCSD <IssrCSD> [1..1]  2345
{Or       OrganisationIdentification <OrgId> [1..1] ± 2345
Or}       CombinedIdentification <CmbndId> [1..1] ± 2345
Or}     InvestorCSD <InvstrCSD> [1..1]  2346
{Or       OrganisationIdentification <OrgId> [1..1] ± 2346
Or}       CombinedIdentification <CmbndId> [1..1] ± 2346
   TechnicalIssuerCSD <TechIssrCSD> [0..1]  2346
{Or     OrganisationIdentification <OrgId> [1..1] ± 2347
Or}     CombinedIdentification <CmbndId> [1..1] ± 2347
   SecurityMaintenance <SctyMntnc> [1..1] Indicator 2347
   IssuanceAccount <IssncAcct> [0..*]  C7, C8,
C10
2347
     IssuanceAccount <IssncAcct> [0..1] ± 2348
     IssuanceBlockChainAddressOrWallet
<IssncBlckChainAdrOrWllt>
[0..1] ± 2348
     PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2349
   DefaultLink <DfltLk> [0..1] Indicator 2349
   ValidFrom <VldFr> [1..1] ± 2349
   ValidTo <VldTo> [0..1] ± 2349
62.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2343 August 2026
```

