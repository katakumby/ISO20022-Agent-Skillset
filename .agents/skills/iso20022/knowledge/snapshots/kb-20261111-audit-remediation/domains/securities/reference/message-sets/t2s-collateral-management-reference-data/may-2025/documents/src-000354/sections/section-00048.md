---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "8.2 Structure"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.075.001.01"]
---

# 8.2 Structure

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblSctiesDeltnReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 53
   EligibleSecurity <ElgblScty> [1..*]  53
     SecurityIdentification <SctyId> [1..*] ± C4, C5,
C6, C7,
C8
53
     CollateralisationCurrency <CollstnCcy> [0..1] CodeSet C1 55
     EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 55
     PartyIdentification <PtyId> [1..1]  55
{Or       OrganisationIdentification <OrgId> [1..1] ± 55
Or}       CombinedIdentification <CmbndId> [1..1] ± 56
   SupplementaryData <SplmtryData> [0..*] ± C9 56
8.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C5 DescriptionUsageRule
Description must be used alone as the last resort.
C6 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 17 April 2025. reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 52 May 2025
```

