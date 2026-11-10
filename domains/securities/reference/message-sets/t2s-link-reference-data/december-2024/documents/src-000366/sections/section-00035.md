---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["5 reda.049.001.01 AccountLinkCreationRequestV01", "5.4 Message Building Blocks"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 5.4 Message Building Blocks

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
5.4.2 AccountLink <AcctLk>
Presence: [1..*]
Definition: Defines how the securities account is linked to the cash account.
Impacted by: C3 "SecuritiesAccountOrBlockChainAddress1Rule", C4
"SecuritiesAccountOrBlockChainAddress2Rule", C5 "SecuritiesAccountOrBlockChainAddress3Rule"
AccountLink <AcctLk> contains the following AccountLink7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccount <SctiesAcct> [0..1] ± 38
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 38
   CashAccount <CshAcct> [1..1] ± 38
   ValidFrom <VldFr> [1..1] ± 39
   ValidTo <VldTo> [0..1] ± 39
   DefaultIndicator <DfltInd> [1..1] Indicator 39
   CollateralisationIndicator <CollstnInd> [1..1] Indicator 39
   CashSettlementIndicator <CshSttlmInd> [1..1] Indicator 40
Constraints
• SecuritiesAccountOrBlockChainAddress1Rule
If SecuritiesAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SecuritiesAccount is present
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 37 December 2024
```

