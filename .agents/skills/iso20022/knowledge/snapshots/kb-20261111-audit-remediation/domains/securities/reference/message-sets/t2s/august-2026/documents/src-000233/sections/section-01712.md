---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "64.2 Structure"]
file_pages: [2360]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2360 to 2360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2360

```text
64.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCSDLkStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2361
     MessageIdentification <MsgId> [1..1] Text 2361
     CreationDateTime <CreDtTm> [0..1] DateTime 2362
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2362
   SecurityCSDLinkStatus <SctyCSDLkSts> [1..1]  C8 2362
     Status <Sts> [1..1] CodeSet 2363
     StatusReason <StsRsn> [0..*]  2363
       Reason <Rsn> [1..1]  2363
{Or         Code <Cd> [1..1] CodeSet 2363
Or}         Proprietary <Prtry> [1..1] Text 2364
       AdditionalInformation <AddtlInf> [0..1] Text 2364
   SecurityCSDLinkIdentification <SctyCSDLkId> [0..1]  2364
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2364
     IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2365
{Or       IssuerCSD <IssrCSD> [1..1]  2366
{Or         OrganisationIdentification <OrgId> [1..1] ± 2366
Or}         CombinedIdentification <CmbndId> [1..1] ± 2366
Or}       InvestorCSD <InvstrCSD> [1..1]  2367
{Or         OrganisationIdentification <OrgId> [1..1] ± 2367
Or}         CombinedIdentification <CmbndId> [1..1] ± 2367
     ValidFrom <VldFr> [1..1] ± 2367
   SupplementaryData <SplmtryData> [0..*] ± C9 2368
64.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2360 August 2026
```

