---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["62 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "62.2 Structure"]
file_pages: [2341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 62.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2341 to 2341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2341

```text
62.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCSDLkCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2342
   SecurityCSDLink <SctyCSDLk> [1..*]  2343
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C9
2343
     IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2344
{Or       IssuerCSD <IssrCSD> [1..1]  2345
{Or         OrganisationIdentification <OrgId> [1..1] ± 2345
Or}         CombinedIdentification <CmbndId> [1..1] ± 2345
Or}       InvestorCSD <InvstrCSD> [1..1]  2346
{Or         OrganisationIdentification <OrgId> [1..1] ± 2346
Or}         CombinedIdentification <CmbndId> [1..1] ± 2346
     TechnicalIssuerCSD <TechIssrCSD> [0..1]  2346
{Or       OrganisationIdentification <OrgId> [1..1] ± 2347
Or}       CombinedIdentification <CmbndId> [1..1] ± 2347
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
   SupplementaryData <SplmtryData> [0..*] ± C11 2350
62.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities 2341 August 2026
```

