---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["7 reda.051.001.01 AccountLinkStatusAdviceV01", "7.2 Structure"]
file_pages: [48]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 7.2 Structure

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 48 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctLkStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  49
     MessageIdentification <MsgId> [1..1] Text 49
     CreationDateTime <CreDtTm> [0..1] DateTime 49
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 49
   AccountLinkStatus <AcctLkSts> [1..1]  C6 50
     Status <Sts> [1..1] CodeSet 50
     StatusReason <StsRsn> [0..*]  50
       Reason <Rsn> [1..1]  51
{Or         Code <Cd> [1..1] CodeSet 51
Or}         Proprietary <Prtry> [1..1] Text 51
       AdditionalInformation <AddtlInf> [0..1] Text 51
   AccountLinkIdentification <AcctLkId> [0..1]  C3, C4,
C5
51
     SecuritiesAccount <SctiesAcct> [0..1] ± 52
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 52
     CashAccount <CshAcct> [1..1] ± 53
     ValidFrom <VldFr> [1..1] ± 53
   SupplementaryData <SplmtryData> [0..*] ± C7 53
7.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C3 SecuritiesAccountOrBlockChainAddress1Rule
If SecuritiesAccount is present, BlockChainAddressOrWallet must be absent.
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 48 December 2024
```

