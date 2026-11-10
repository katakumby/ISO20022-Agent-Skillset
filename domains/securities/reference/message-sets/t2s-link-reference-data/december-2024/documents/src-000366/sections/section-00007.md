---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecurityCSDLink <SctyCSDLk>"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 2.4.2 SecurityCSDLink <SctyCSDLk>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
2.4.2 SecurityCSDLink <SctyCSDLk>
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
9
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  10
{Or     IssuerCSD <IssrCSD> [1..1]  11
{Or       OrganisationIdentification <OrgId> [1..1] ± 11
Or}       CombinedIdentification <CmbndId> [1..1] ± 11
Or}     InvestorCSD <InvstrCSD> [1..1]  12
{Or       OrganisationIdentification <OrgId> [1..1] ± 12
Or}       CombinedIdentification <CmbndId> [1..1] ± 12
   TechnicalIssuerCSD <TechIssrCSD> [0..1]  12
{Or     OrganisationIdentification <OrgId> [1..1] ± 13
Or}     CombinedIdentification <CmbndId> [1..1] ± 13
   SecurityMaintenance <SctyMntnc> [1..1] Indicator 13
   IssuanceAccount <IssncAcct> [0..*]  C7, C8,
C10
13
     IssuanceAccount <IssncAcct> [0..1] ± 14
     IssuanceBlockChainAddressOrWallet
<IssncBlckChainAdrOrWllt>
[0..1] ± 14
     PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 15
   DefaultLink <DfltLk> [0..1] Indicator 15
   ValidFrom <VldFr> [1..1] ± 15
   ValidTo <VldTo> [0..1] ± 15
2.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 9 December 2024
```

