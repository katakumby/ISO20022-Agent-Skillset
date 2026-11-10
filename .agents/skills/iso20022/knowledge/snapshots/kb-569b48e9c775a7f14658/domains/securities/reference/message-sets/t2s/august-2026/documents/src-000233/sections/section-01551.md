---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["45 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "45.2 Structure"]
file_pages: [2174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.025.001.01"]
---

# 45.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2174 to 2174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2174

```text
45.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblSctiesCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2175
   EligibleSecurity <ElgblScty> [1..*]  2175
     SecurityIdentification <SctyId> [1..*] ± C4, C5,
C6, C7,
C8
2175
     CollateralisationCurrency <CollstnCcy> [0..1] CodeSet C1 2177
     EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 2177
     PartyIdentification <PtyId> [1..1]  2177
{Or       OrganisationIdentification <OrgId> [1..1] ± 2177
Or}       CombinedIdentification <CmbndId> [1..1] ± 2178
   SupplementaryData <SplmtryData> [0..*] ± C9 2178
45.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.025.001.01
EligibleSecuritiesCreationRequestV01
Target2-Securities 2174 August 2026
```

