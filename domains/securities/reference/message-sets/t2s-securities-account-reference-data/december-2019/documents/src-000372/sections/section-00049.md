---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>", "6.4.3.2.1.3 NegativePosition <NegPos>"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.4.3.2.1.3 NegativePosition <NegPos>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
Definition: Indicates whether the securities account is on hold or not.
Usage:
- Meaning when true: account is in hold status.
- Meaning when false: account is in release status.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 98):
• Meaning When True: True
• Meaning When False: False
6.4.3.2.1.3  NegativePosition <NegPos>
Presence: [0..1]
Definition: Indicates whether the securities account can hold a negative position in a security or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 98):
• Meaning When True: True
• Meaning When False: False
6.4.3.2.1.4  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 99
6.4.3.2.1.5  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 99
6.4.3.2.2  SystemRestriction <SysRstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
SystemRestriction <SysRstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 53
   ValidTo <VldTo> [0..1] DateTime 54
   Type <Tp> [1..1] Text 54
6.4.3.2.2.1  ValidFrom <VldFr>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 53 December 2019
```

