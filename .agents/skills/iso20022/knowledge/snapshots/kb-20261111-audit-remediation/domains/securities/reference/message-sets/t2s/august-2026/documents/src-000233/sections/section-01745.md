---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["69 reda.077.001.01 CloseLinkDeletionRequestV01", "69.2 Structure"]
file_pages: [2396]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.077.001.01"]
---

# 69.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2396 to 2396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2396

```text
69.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ClsLkDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2397
   CloseLink <ClsLk> [1..*]  2397
     SecurityIdentification <SctyId> [1..*] ± C3, C4,
C5, C6,
C7
2397
     PartyIdentification <PtyId> [1..1]  2398
{Or       OrganisationIdentification <OrgId> [1..1] ± 2399
Or}       CombinedIdentification <CmbndId> [1..1] ± 2399
     CreditProviderIdentification <CdtPrvdrId> [0..1]  2399
{Or       OrganisationIdentification <OrgId> [1..1] ± 2400
Or}       CombinedIdentification <CmbndId> [1..1] ± 2400
   SupplementaryData <SplmtryData> [0..*] ± C8 2400
69.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.077.001.01 CloseLinkDeletionRequestV01
Target2-Securities 2396 August 2026
```

