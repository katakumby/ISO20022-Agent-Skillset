---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["67 reda.051.001.01 AccountLinkStatusAdviceV01", "67.2 Structure"]
file_pages: [2382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 67.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2382 to 2382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2382

```text
67.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctLkStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2383
     MessageIdentification <MsgId> [1..1] Text 2383
     CreationDateTime <CreDtTm> [0..1] DateTime 2383
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2383
   AccountLinkStatus <AcctLkSts> [1..1]  C6 2384
     Status <Sts> [1..1] CodeSet 2384
     StatusReason <StsRsn> [0..*]  2384
       Reason <Rsn> [1..1]  2385
{Or         Code <Cd> [1..1] CodeSet 2385
Or}         Proprietary <Prtry> [1..1] Text 2385
       AdditionalInformation <AddtlInf> [0..1] Text 2385
   AccountLinkIdentification <AcctLkId> [0..1]  C3, C4,
C5
2385
     SecuritiesAccount <SctiesAcct> [0..1] ± 2386
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2386
     CashAccount <CshAcct> [1..1] ± 2387
     ValidFrom <VldFr> [1..1] ± 2387
   SupplementaryData <SplmtryData> [0..*] ± C7 2387
67.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2382 August 2026
```

