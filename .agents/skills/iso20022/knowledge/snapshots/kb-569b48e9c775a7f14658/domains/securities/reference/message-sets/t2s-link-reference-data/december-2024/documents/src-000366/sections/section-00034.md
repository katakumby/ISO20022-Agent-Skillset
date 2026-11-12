---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["5 reda.049.001.01 AccountLinkCreationRequestV01", "5.2 Structure"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 5.2 Structure

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctLkCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 37
   AccountLink <AcctLk> [1..*]  C3, C4,
C5
37
     SecuritiesAccount <SctiesAcct> [0..1] ± 38
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 38
     CashAccount <CshAcct> [1..1] ± 38
     ValidFrom <VldFr> [1..1] ± 39
     ValidTo <VldTo> [0..1] ± 39
     DefaultIndicator <DfltInd> [1..1] Indicator 39
     CollateralisationIndicator <CollstnInd> [1..1] Indicator 39
     CashSettlementIndicator <CshSttlmInd> [1..1] Indicator 40
   SupplementaryData <SplmtryData> [0..*] ± C6 40
5.3 Constraints
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
C4 SecuritiesAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SecuritiesAccount must be absent.
C5 SecuritiesAccountOrBlockChainAddress3Rule
Either SecuritiesAccount or BlockChainAddressOrWallet must be present but not both.
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 36 December 2024
```

