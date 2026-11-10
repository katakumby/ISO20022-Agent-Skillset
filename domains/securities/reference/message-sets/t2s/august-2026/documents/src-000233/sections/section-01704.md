---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "63.2 Structure"]
file_pages: [2352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 63.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2352 to 2352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2352

```text
63.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCSDLkMntncReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2353
   SecurityCSDLinkIdentification <SctyCSDLkId> [1..1]  2353
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2354
     IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2355
{Or       IssuerCSD <IssrCSD> [1..1]  2355
{Or         OrganisationIdentification <OrgId> [1..1] ± 2356
Or}         CombinedIdentification <CmbndId> [1..1] ± 2356
Or}       InvestorCSD <InvstrCSD> [1..1]  2356
{Or         OrganisationIdentification <OrgId> [1..1] ± 2356
Or}         CombinedIdentification <CmbndId> [1..1] ± 2357
     ValidFrom <VldFr> [1..1] ± 2357
   Update <Upd> [1..1]  2357
     DefaultLink <DfltLk> [0..1] Indicator 2357
     ValidTo <VldTo> [1..1] ± 2358
   SupplementaryData <SplmtryData> [0..*] ± C8 2358
63.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities 2352 August 2026
```

