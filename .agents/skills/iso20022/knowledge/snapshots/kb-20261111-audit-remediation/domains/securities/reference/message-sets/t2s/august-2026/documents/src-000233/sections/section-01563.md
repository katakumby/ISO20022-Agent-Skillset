---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["47 reda.027.001.01 CloseLinkCreationRequestV01", "47.2 Structure"]
file_pages: [2188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 47.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2188 to 2188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2188

```text
47.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ClsLkCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2189
   CloseLink <ClsLk> [1..1]  2189
     SecurityIdentification <SctyId> [1..*] ± C3, C4,
C5, C6,
C7
2189
     PartyIdentification <PtyId> [1..1]  2190
{Or       OrganisationIdentification <OrgId> [1..1] ± 2191
Or}       CombinedIdentification <CmbndId> [1..1] ± 2191
     CreditProviderIdentification <CdtPrvdrId> [0..1]  2191
{Or       OrganisationIdentification <OrgId> [1..1] ± 2192
Or}       CombinedIdentification <CmbndId> [1..1] ± 2192
   SupplementaryData <SplmtryData> [0..*] ± C8 2192
47.3 Constraints
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
reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities 2188 August 2026
```

