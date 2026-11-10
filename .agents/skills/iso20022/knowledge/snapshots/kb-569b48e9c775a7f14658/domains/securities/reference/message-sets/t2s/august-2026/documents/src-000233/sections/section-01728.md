---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["66 reda.050.001.01 AccountLinkMaintenanceRequestV01", "66.2 Structure"]
file_pages: [2376]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 66.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2376 to 2376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2376

```text
66.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctLkMntncReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2377
   AccountLinkIdentification <AcctLkId> [1..1]  C3, C4,
C5
2377
     SecuritiesAccount <SctiesAcct> [0..1] ± 2378
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2378
     CashAccount <CshAcct> [1..1] ± 2378
     ValidFrom <VldFr> [1..1] ± 2378
   Update <Upd> [1..1]  2379
     ValidTo <VldTo> [1..1] ± 2379
   SupplementaryData <SplmtryData> [0..*] ± C6 2379
66.3 Constraints
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
66.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2376 August 2026
```

