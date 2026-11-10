---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["4 reda.038.001.01 CashAccountActivityAdviceV01", "4.3 Constraints"]
file_pages: [109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.038.001.01"]
---

# 4.3 Constraints

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 109 to 109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
4.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C3 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C4 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 147 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 148
   CreationDateTime <CreDtTm> [0..1] DateTime 148
4.4.2 CashAccountActivity <CshAcctActvty>
Presence: [1..1]
Definition: Activity report of changes occurred for a cash account defined in the system.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.038.001.01 CashAccountActivityAdviceV01
Target2-Securities - Cash Account Query and Report 109 August 2026
```

