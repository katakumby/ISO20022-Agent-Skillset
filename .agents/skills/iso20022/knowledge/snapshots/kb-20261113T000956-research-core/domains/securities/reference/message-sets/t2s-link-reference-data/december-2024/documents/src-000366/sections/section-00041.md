---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "6.4 Message Building Blocks", "6.4.1 MessageHeader <MsgHdr>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 6.4.1 MessageHeader <MsgHdr>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
6.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
6.4.2 AccountLinkIdentification <AcctLkId>
Presence: [1..1]
Definition: Provides a unique and unambiguous identification for the account link.
Impacted by: C3 "SecuritiesAccountOrBlockChainAddress1Rule", C4
"SecuritiesAccountOrBlockChainAddress2Rule", C5 "SecuritiesAccountOrBlockChainAddress3Rule"
AccountLinkIdentification <AcctLkId> contains the following AccountLink8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesAccount <SctiesAcct> [0..1] ± 44
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 44
   CashAccount <CshAcct> [1..1] ± 44
   ValidFrom <VldFr> [1..1] ± 44
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
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 43 December 2024
```

