---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "4.2 Structure"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4.2 Structure

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyCSDLkStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  27
     MessageIdentification <MsgId> [1..1] Text 27
     CreationDateTime <CreDtTm> [0..1] DateTime 28
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 28
   SecurityCSDLinkStatus <SctyCSDLkSts> [1..1]  C8 28
     Status <Sts> [1..1] CodeSet 29
     StatusReason <StsRsn> [0..*]  29
       Reason <Rsn> [1..1]  29
{Or         Code <Cd> [1..1] CodeSet 29
Or}         Proprietary <Prtry> [1..1] Text 30
       AdditionalInformation <AddtlInf> [0..1] Text 30
   SecurityCSDLinkIdentification <SctyCSDLkId> [0..1]  30
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
30
     IssuerInvestorCSD <IssrInvstrCSD> [1..1]  31
{Or       IssuerCSD <IssrCSD> [1..1]  32
{Or         OrganisationIdentification <OrgId> [1..1] ± 32
Or}         CombinedIdentification <CmbndId> [1..1] ± 32
Or}       InvestorCSD <InvstrCSD> [1..1]  33
{Or         OrganisationIdentification <OrgId> [1..1] ± 33
Or}         CombinedIdentification <CmbndId> [1..1] ± 33
     ValidFrom <VldFr> [1..1] ± 33
   SupplementaryData <SplmtryData> [0..*] ± C9 34
4.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 26 December 2024
```

