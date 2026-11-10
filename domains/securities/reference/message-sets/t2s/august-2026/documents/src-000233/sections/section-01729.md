---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["66 reda.050.001.01 AccountLinkMaintenanceRequestV01", "66.4 Message Building Blocks", "66.4.1 MessageHeader <MsgHdr>"]
file_pages: [2377]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 66.4.1 MessageHeader <MsgHdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2377 to 2377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2377

```text
66.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
66.4.2 AccountLinkIdentification <AcctLkId>
Presence: [1..1]
Definition: Provides a unique and unambiguous identification for the account link.
Impacted by: C3 "SecuritiesAccountOrBlockChainAddress1Rule", C4
"SecuritiesAccountOrBlockChainAddress2Rule", C5 "SecuritiesAccountOrBlockChainAddress3Rule"
AccountLinkIdentification <AcctLkId> contains the following AccountLink8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccount <SctiesAcct> [0..1] ± 2378
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2378
   CashAccount <CshAcct> [1..1] ± 2378
   ValidFrom <VldFr> [1..1] ± 2378
Constraints
• SecuritiesAccountOrBlockChainAddress1Rule
If SecuritiesAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SecuritiesAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SecuritiesAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SecuritiesAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SecuritiesAccount Must be absent
• SecuritiesAccountOrBlockChainAddress3Rule
Either SecuritiesAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SecuritiesAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2377 August 2026
```

