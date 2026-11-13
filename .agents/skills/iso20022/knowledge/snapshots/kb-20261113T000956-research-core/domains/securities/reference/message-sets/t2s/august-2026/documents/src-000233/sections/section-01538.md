---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.4 Message Building Blocks", "43.4.3 Modification <Mod>", "43.4.3.2 RequestedModification <ReqdMod>", "43.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>", "43.4.3.2.1.3 NegativePosition <NegPos>"]
file_pages: [2160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.4.3.2.1.3 NegativePosition <NegPos>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2160 to 2160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2160

```text
Definition: Indicates whether the securities account is on hold or not.
Usage:
- Meaning when true: account is in hold status.
- Meaning when false: account is in release status.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
43.4.3.2.1.3  NegativePosition <NegPos>
Presence: [0..1]
Definition: Indicates whether the securities account can hold a negative position in a security or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
43.4.3.2.1.4  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 3325
43.4.3.2.1.5  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 3325
43.4.3.2.2  SystemRestriction <SysRstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
SystemRestriction <SysRstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 2160
   ValidTo <VldTo> [0..1] DateTime 2161
   Type <Tp> [1..1] Text 2161
43.4.3.2.2.1  ValidFrom <VldFr>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2160 August 2026
```

