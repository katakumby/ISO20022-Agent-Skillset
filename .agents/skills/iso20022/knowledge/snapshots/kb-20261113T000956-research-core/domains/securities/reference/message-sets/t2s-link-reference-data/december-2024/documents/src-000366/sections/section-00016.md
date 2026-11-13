---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.2 Structure"]
file_pages: [18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.2 Structure

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 18 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 18

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCSDLkMntncReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 19
   SecurityCSDLinkIdentification <SctyCSDLkId> [1..1]  19
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
20
     IssuerInvestorCSD <IssrInvstrCSD> [1..1]  21
{Or       IssuerCSD <IssrCSD> [1..1]  21
{Or         OrganisationIdentification <OrgId> [1..1] ± 22
Or}         CombinedIdentification <CmbndId> [1..1] ± 22
Or}       InvestorCSD <InvstrCSD> [1..1]  22
{Or         OrganisationIdentification <OrgId> [1..1] ± 22
Or}         CombinedIdentification <CmbndId> [1..1] ± 23
     ValidFrom <VldFr> [1..1] ± 23
   Update <Upd> [1..1]  23
     DefaultLink <DfltLk> [0..1] Indicator 23
     ValidTo <VldTo> [1..1] ± 24
   SupplementaryData <SplmtryData> [0..*] ± C8 24
3.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 18 December 2024
```

