---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["5 reda.027.001.01 CloseLinkCreationRequestV01", "5.2 Structure"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 5.2 Structure

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ClsLkCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 32
   CloseLink <ClsLk> [1..1]  32
     SecurityIdentification <SctyId> [1..*] ± C3, C4,
C5, C6,
C7
32
     PartyIdentification <PtyId> [1..1]  33
{Or       OrganisationIdentification <OrgId> [1..1] ± 34
Or}       CombinedIdentification <CmbndId> [1..1] ± 34
     CreditProviderIdentification <CdtPrvdrId> [0..1]  34
{Or       OrganisationIdentification <OrgId> [1..1] ± 35
Or}       CombinedIdentification <CmbndId> [1..1] ± 35
   SupplementaryData <SplmtryData> [0..*] ± C8 35
5.3 Constraints
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
C5 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C6 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 17 April 2025. reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities - Collateral Management Reference Data 31 May 2025
```

