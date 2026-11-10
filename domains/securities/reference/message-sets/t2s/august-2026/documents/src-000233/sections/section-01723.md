---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["65 reda.049.001.01 AccountLinkCreationRequestV01", "65.4 Message Building Blocks"]
file_pages: [2371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 65.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2371 to 2371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2371

```text
65.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
65.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
65.4.2 AccountLink <AcctLk>
Presence: [1..*]
Definition: Defines how the securities account is linked to the cash account.
Impacted by: C3 "SecuritiesAccountOrBlockChainAddress1Rule", C4
"SecuritiesAccountOrBlockChainAddress2Rule", C5 "SecuritiesAccountOrBlockChainAddress3Rule"
AccountLink <AcctLk> contains the following AccountLink7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccount <SctiesAcct> [0..1] ± 2372
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2372
   CashAccount <CshAcct> [1..1] ± 2372
   ValidFrom <VldFr> [1..1] ± 2373
   ValidTo <VldTo> [0..1] ± 2373
   DefaultIndicator <DfltInd> [1..1] Indicator 2373
   CollateralisationIndicator <CollstnInd> [1..1] Indicator 2373
   CashSettlementIndicator <CshSttlmInd> [1..1] Indicator 2374
Constraints
• SecuritiesAccountOrBlockChainAddress1Rule
If SecuritiesAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SecuritiesAccount is present
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2371 August 2026
```

